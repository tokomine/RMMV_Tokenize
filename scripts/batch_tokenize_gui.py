import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QMessageBox
)
from rmmv_tokenize.batch_tokenize import BatchJapaneseTokenizer

class BatchTokenizeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Batch Japanese Tokenizer')
        self.resize(500, 180)
        self.init_ui()

    def init_ui(self):
        # 输入目录
        self.input_label = QLabel('输入文件夹:')
        self.input_edit = QLineEdit()
        self.input_btn = QPushButton('选择')
        self.input_btn.clicked.connect(self.select_input_dir)

        # 输出CSV
        self.output_label = QLabel('输出CSV路径:')
        self.output_edit = QLineEdit()
        self.output_btn = QPushButton('选择')
        self.output_btn.clicked.connect(self.select_output_file)

        # 执行按钮
        self.run_btn = QPushButton('执行')
        self.run_btn.clicked.connect(self.run_batch_tokenize)

        # 布局
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_edit)
        input_layout.addWidget(self.input_btn)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_edit)
        output_layout.addWidget(self.output_btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_label)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.output_label)
        main_layout.addLayout(output_layout)
        main_layout.addWidget(self.run_btn)

        self.setLayout(main_layout)

    def select_input_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, '选择输入文件夹')
        if dir_path:
            self.input_edit.setText(dir_path)

    def select_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, '选择输出CSV文件', filter='CSV Files (*.csv)')
        if file_path:
            self.output_edit.setText(file_path)

    def run_batch_tokenize(self):
        input_dir = self.input_edit.text().strip()
        output_csv = self.output_edit.text().strip()
        if not input_dir or not os.path.isdir(input_dir):
            QMessageBox.warning(self, '错误', '请输入有效的输入文件夹路径')
            return
        if not output_csv:
            QMessageBox.warning(self, '错误', '请输入有效的输出CSV路径')
            return
        try:
            tokenizer = BatchJapaneseTokenizer(input_dir, output_csv)
            tokenizer.process()
            QMessageBox.information(self, '完成', f'处理完成，结果已保存到：\n{output_csv}')
        except Exception as e:
            QMessageBox.critical(self, '异常', f'处理时发生错误：\n{e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BatchTokenizeGUI()
    gui.show()
    sys.exit(app.exec_())
