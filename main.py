import csv
import os
import openpyxl

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QDate
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QDialog, QMainWindow, QWidget, \
    QDialogButtonBox
from PyQt6.uic import loadUi
from dotenv import load_dotenv

from Database import Database


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.table_name = self.parent().db_table_n
        self.setWindowTitle("Add Data")
        self.setWindowIcon(QIcon('icons\\add.ico'))
        self.layout = QtWidgets.QFormLayout(self)
        self.line_edits = []
        self.column_mapping = {}
        line_edit_idx = 0
        for idx, column_name in enumerate(self.parent().table_data[0]):
            if (self.table_name == "orders" and column_name.lower() == "price") \
                    or column_name.lower() in ["id", "salt"]:
                continue
            if column_name.lower() == "apartment":
                combobox = QtWidgets.QComboBox()
                self.line_edits.append(combobox)
                self.layout.addRow(column_name, combobox)
                self.column_mapping[column_name] = line_edit_idx
                for apartment_id in self.parent().database.get_available_apartments():
                    combobox.addItem(str(apartment_id[0]))
            else:
                line_edit = QtWidgets.QLineEdit()
                self.line_edits.append(line_edit)
                self.layout.addRow(column_name, line_edit)
                self.column_mapping[column_name] = line_edit_idx
            line_edit_idx += 1

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
                                   parent=self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addRow(buttons)

    def get_data(self):
        columns = []
        values = []
        for column_name, line_edit_idx in self.column_mapping.items():
            line_edit = self.line_edits[line_edit_idx]
            if isinstance(line_edit, QtWidgets.QComboBox):
                selected_item = line_edit.currentText()
                if selected_item:
                    columns.append(column_name)
                    values.append(selected_item)
            elif line_edit.text().strip():
                columns.append(column_name)
                values.append("'{}'".format(line_edit.text()))
        if self.table_name == 'useraccount':
            if self.parent().role != 1:
                return
            existing_user = self.parent().database.select_data("useraccount",
                                                               condition=f"login = '{self.line_edits[self.column_mapping['login']].text().strip()}'")
            if existing_user:
                QMessageBox.warning(self, "Add", "User already exists")
                return
            return columns, [self.line_edits[self.column_mapping['login']].text().strip(),
                             self.line_edits[self.column_mapping['h_password']].text().strip(),
                             self.line_edits[self.column_mapping['role']].text().strip()]
        return columns, values


class MainWindow(QMainWindow):
    def __init__(self, login_window, database):
        super().__init__()
        loadUi("mainWindow.ui", self)
        self.setWindowTitle("Main Window")
        self.setWindowIcon(QIcon('icons\\main_window.ico'))
        self.animation = None
        self.table_data = None
        self.db_table_n = None
        self.login = None
        self.button = None
        self.role = None
        self.database = database
        self.button_connects(login_window)

    def button_connects(self, login_window):
        self.b_logout.clicked.connect(lambda: self.switch_to_login(login_window))
        self.b_menu.clicked.connect(lambda: self.slide_left_menu())
        self.b_orders.clicked.connect(lambda: self.switch_to_table("orders"))
        self.b_logs.clicked.connect(lambda: self.switch_to_table("logs"))
        self.b_useraccount.clicked.connect(lambda: self.switch_to_table("useraccount"))
        self.b_apartment_d.clicked.connect(lambda: self.switch_to_table("apartment_d"))
        self.b_guest_d.clicked.connect(lambda: self.switch_to_table("guest_d"))
        self.b_discount.clicked.connect(lambda: self.switch_to_table("discount"))
        self.b_role.clicked.connect(lambda: self.switch_to_table("role"))
        self.b_staff_d.clicked.connect(lambda: self.switch_to_table("staff_d"))
        self.b_rs_refresh.clicked.connect(self.populate_table)
        self.le_h_search.textChanged.connect(self.search)
        self.e_excel.triggered.connect(lambda: self.export_data("excel"))
        self.e_csv.triggered.connect(lambda: self.export_data("csv"))
        self.b_rs_delete.clicked.connect(self.delete_selected_data)
        self.b_rs_add.clicked.connect(self.show_add_dialog)
        self.b_rs_update.clicked.connect(self.update_data_table)

    def set_role(self, role):
        self.role = role
        self.db_table_n = None
        self.table_data = None
        button_visibility = {
            None: [False] * 8,
            1: [True] * 8,
            2: [True] * 6 + 2 * [False],
        }.get(role, [True] * 4 + [False] * 4)
        self.b_orders.setVisible(button_visibility[0])
        self.b_apartment_d.setVisible(button_visibility[1])
        self.b_guest_d.setVisible(button_visibility[2])
        self.b_discount.setVisible(button_visibility[3])
        self.b_logs.setVisible(button_visibility[4])
        self.b_useraccount.setVisible(button_visibility[5])
        self.b_role.setVisible(button_visibility[6])
        self.b_staff_d.setVisible(button_visibility[7])
        self.reset_button_style()

    def delete_selected_data(self):
        if self.table_data and self.table is None:
            return
        selected_items = self.table.selectedItems()
        if not selected_items:
            return
        reply = QMessageBox.question(
            self,
            "Delete Data",
            "Are you sure you want to delete the selected data?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        rows_to_delete = {item.row() for item in selected_items}
        deleted_data = []
        for row in sorted(rows_to_delete, reverse=True):
            deleted_row_data = [
                self.table.item(row, col).text()
                for col in range(self.table.columnCount())
            ]
            deleted_data.append(deleted_row_data)
            condition = f"id = '{deleted_row_data[0]}'"
            if self.db_table_n != 'logs':
                log_data = "'" + ";".join(deleted_row_data) + "'"
                self.database.insert_data(
                    'logs',
                    ['data_', 'user_', 'table_', 'action_'],
                    [log_data, "'" + self.login + "'", "'" + self.db_table_n + "'", "'delete'"]
                )
            elif deleted_row_data[-1] == 'delete':
                self.database.insert_data(
                    deleted_row_data[3],
                    self.database.get_table_data(deleted_row_data[3])[0],
                    [i if i.isdigit() or i is None else "'" + i + "'"
                     for i in deleted_row_data[4].split(';')
                     ]
                )
            else:
                continue
            self.database.delete_data(self.db_table_n, condition)
        QMessageBox.information(
            self,
            "Delete Data",
            f"Deleted {len(deleted_data)} rows of data:\n\n{deleted_data}"
        )
        self.populate_table()

    def update_data_table(self):
        if self.table_data and self.table is None:
            return
        column_names = self.table_data[0]
        primary_key_column = column_names[0]
        db_data = self.database.select_data(self.db_table_n, column_names)
        for row in range(self.table.rowCount()):
            change_check = False
            for col in range(self.table.columnCount()):
                current_data = self.table.item(row, col).text()
                db_data_value = db_data[row][col]
                if str(current_data) != str(db_data_value) \
                        and current_data is not None \
                        and self.table.horizontalHeaderItem(col).text() not in ['id', 'salt'] \
                        and self.db_table_n != 'logs':
                    change_check = True
                    if self.table.horizontalHeaderItem(col).text() not in ['h_password', 'role']:
                        condition = f"{primary_key_column} = {self.table.item(row, 0).text()}"
                        values = {self.table.horizontalHeaderItem(col).text(): current_data}
                        if self.table.horizontalHeaderItem(col).text() == 'role' and self.role != 1:
                            change_check = False
                            continue
                        self.database.update_data(self.db_table_n, values, condition)
                    elif self.login == self.table.item(row, 1).text() \
                            and self.table.horizontalHeaderItem(col).text() == 'h_password':
                        self.database.change_password(self.table.item(row, 0).text(), current_data)
                    else:
                        change_check = False
            if change_check:
                log_data = "'" + ";".join(str(d) for d in db_data[row]) + "'"
                self.database.insert_data(
                    'logs',
                    ['data_', 'user_', 'table_', 'action_'],
                    [log_data, "'" + self.login + "'", "'" + self.db_table_n + "'", "'update'"]
                )
        self.populate_table()

    def slide_left_menu(self):
        new_width = 100 if self.left_side_menu.width() == 50 else 50
        self.animation = QPropertyAnimation(self.left_side_menu, b"minimumWidth", self)
        self.animation.setDuration(200)
        self.animation.setStartValue(self.left_side_menu.width())
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def switch_to_table(self, table_name):
        self.le_h_search.setText("")
        self.db_table_n = table_name
        if self.button is not None:
            self.button.setStyleSheet("")
            self.table.clear()
            self.table.horizontalHeader().setSortIndicator(-1, Qt.SortOrder.AscendingOrder)
        self.button = getattr(self, "b_" + table_name)
        self.button.setStyleSheet("QPushButton { font-weight: bold; color: white;background-color: #3c4f62; }")
        self.populate_table()

    def reset_button_style(self):
        self.b_orders.setStyleSheet("")
        self.b_apartment_d.setStyleSheet("")
        self.b_guest_d.setStyleSheet("")
        self.b_discount.setStyleSheet("")
        self.b_role.setStyleSheet("")
        self.b_logs.setStyleSheet("")
        self.b_useraccount.setStyleSheet("")
        self.b_staff_d.setStyleSheet("")

    def search(self, s):
        if self.table_data and self.table is None:
            return
        self.table.setCurrentItem(None)
        if not s:
            return
        matching_items = self.table.findItems(s, Qt.MatchFlag.MatchContains)
        if matching_items:
            for item in matching_items:
                item.setSelected(True)

    def populate_table(self, leave=False):
        if self.db_table_n:
            self.table.clearContents()
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.table.setHorizontalHeaderLabels([])
            if leave:
                return
            # if self.db_table_n=='logs':
            self.table_data = self.database.get_table_data(self.db_table_n)
            column_names, rows = self.table_data
            self.table.setColumnCount(len(column_names))
            self.table.setHorizontalHeaderLabels(column_names)
            self.table.horizontalHeader().setVisible(True)
            self.table.setRowCount(len(rows))

            for row_idx, row_data in enumerate(rows):
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem()
                    if isinstance(cell_data, QDate):
                        item.setData(Qt.ItemDataRole.EditRole, cell_data)
                    elif isinstance(cell_data, (int, float)):
                        item.setData(Qt.ItemDataRole.EditRole, cell_data)
                    else:
                        item.setData(Qt.ItemDataRole.EditRole, str(cell_data))
                    self.table.setItem(row_idx, col_idx, item)

    def show_add_dialog(self):
        if self.table_data is not None and self.db_table_n != 'logs':
            dialog = AddDialog(self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                data = dialog.get_data()
                if data is not None:
                    if self.db_table_n == "useraccount":
                        self.database.create_user(data[1][0], data[1][1], data[1][2])
                        self.populate_table()
                        return
                    self.database.insert_data(self.db_table_n, data[0], data[1])
            self.populate_table()

    def export_data(self, file_format):
        if self.table_data is None or self.db_table_n is None or self.table is None:
            return
        if file_format == "excel":
            file_dialog_title = "Save Excel File"
            file_extension = "xlsx"
        else:
            file_dialog_title = "Save CSV File"
            file_extension = "csv"
        file_filter = f"{file_format.capitalize()} Files (*.{file_extension})"
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, file_dialog_title, "", file_filter)

        if file_path:
            if file_format == "excel":
                self.export_data_to_excel(file_path)
            elif file_format == "csv":
                self.export_data_to_csv(file_path)

            QMessageBox.information(self, f"Export to {file_format.capitalize()}",
                                    f"Data exported to {file_format.capitalize()} successfully.")

    def export_data_to_excel(self, file_path):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        header_row = self.table_data[0]
        data_rows = self.table_data[1]
        worksheet.append(header_row)
        for row in data_rows:
            worksheet.append(row)
        workbook.save(file_path)
        self.show_export_success_message(file_path)

    def export_data_to_csv(self, file_path):
        with open(file_path, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.table_data[0])
            csvwriter.writerows(self.table_data[1])
        self.show_export_success_message(file_path)

    def show_export_success_message(self, file_path):
        QMessageBox.information(self, "Export Successful", f"The table has been exported to:\n{file_path}")

    def set_login(self, login):
        self.login = login
        self.set_role(self.database.get_user_role(self.login))

    def switch_to_login(self, login_window):
        self.populate_table(True)
        self.hide()
        login_window.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


class LogInWindow(QWidget):
    def __init__(self, database):
        super().__init__()
        loadUi("logIn.ui", self)
        self.setWindowTitle("Log In")
        self.setWindowIcon(QIcon('icons\\log_in.ico'))
        self.database = database
        self.li_b_log_in.clicked.connect(self.log_in)
        self.li_b_sign_up.clicked.connect(self.switch_to_signup)
        self.main_window = None

    def log_in(self):
        login = self.li_login.text().replace(" ", "")
        password = self.li_password.text().replace(" ", "")

        self.li_login.clear()
        self.li_password.clear()
        if not login or not password:
            QMessageBox.warning(self, "icons\\Log in", "Please enter a valid username and password")
            return
        if self.database.authenticate_user(login, password):
            QMessageBox.information(self, "Log In", f"Logged in as {login}")
            self.hide()
            if self.main_window is None:
                self.main_window = MainWindow(self, database)
            self.main_window.set_login(login)
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Log In", "Invalid login or password")

    def switch_to_signup(self):
        signup_window.show()
        self.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


class SignUpWindow(QWidget):
    def __init__(self, database):
        super().__init__()
        loadUi("signUp.ui", self)
        self.setWindowTitle("Sign Up")
        self.setWindowIcon(QIcon('icons\\sign_up.ico'))
        self.database = database
        self.su_b_sign_up.clicked.connect(self.sign_up)
        self.su_b_login_in.clicked.connect(self.switch_to_login)

    def sign_up(self):
        login = self.su_login.text().replace(" ", "")
        password = self.su_password.text().replace(" ", "")
        re_password = self.su_password_2.text().replace(" ", "")
        if not login or not password or not re_password:
            QMessageBox.warning(self, "Sign Up", "Please enter a valid username and password")
            return
        if password != re_password:
            QMessageBox.warning(self, "Sign Up", "Passwords do not match")
            return
        else:
            existing_user = self.database.select_data("useraccount", condition=f"login = '{login}'")
            if existing_user:
                QMessageBox.warning(self, "Sign Up", "User already exists")
                return
            if self.database.create_user(login, password):
                QMessageBox.information(self, "Sign Up", "User created successfully")
            else:
                QMessageBox.warning(self, "Sign Up", "Failed to create user")
        self.su_login.clear()
        self.su_password.clear()
        self.su_password_2.clear()

    def switch_to_login(self):
        login_window.show()
        self.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    load_dotenv()
    database = Database(database=os.getenv("DATABASE"), user=os.getenv("USER"),
                        password=os.getenv("PASSWORD"), host=os.getenv("HOST"))
    app = QApplication([])
    login_window = LogInWindow(database)
    signup_window = SignUpWindow(database)
    login_window.show()
    app.exec()
    database.close()
