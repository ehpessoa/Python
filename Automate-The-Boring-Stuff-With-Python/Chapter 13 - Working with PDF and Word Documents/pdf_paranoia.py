#! python3
# pdf_paranoia.py
# usage: python pdf_paranoia {encrypt or decrypt} {folder_path} {password}

import os
import sys
import PyPDF2
from PyPDF2.utils import PdfReadError


def encrypt(folder_path, password):
    """
    Encrypts all pdf files in given directory with given password
    :param folder_path: String
    :param password: String
    :return: None
    """
    os.chdir(folder_path)
    for root, dir_names, file_names in os.walk('.'):
        for file in file_names:
            if file.endswith('.pdf'):
                pdf_file = open(os.path.abspath(os.path.join(root, file)), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                pdf_writer = PyPDF2.PdfFileWriter()
                encrypted_pdf_name = f'{file[:-4]}_encrypted.pdf'
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))
                pdf_writer.encrypt(password)
                result_pdf = open(os.path.abspath(os.path.join(root, encrypted_pdf_name)), 'wb')
                pdf_writer.write(result_pdf)
                print(f'Encrypted {encrypted_pdf_name}')
                result_pdf.close()
                pdf_file.close()


def decrypt(folder_path, password):
    """
    Decrypts all pdf files in given directory with given password
    :param folder_path: String
    :param password: String
    :return: None
    """
    os.chdir(folder_path)
    for root, dir_names, file_names in os.walk('.'):
        for file in file_names:
            if file.endswith('.pdf'):
                pdf_file = open(os.path.abspath(os.path.join(root, file)), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                if pdf_reader.isEncrypted:
                    try:
                        pdf_reader.decrypt(password)
                        pdf_writer = PyPDF2.PdfFileWriter()
                        unencrypted_pdf_name = f'{file[:-4]}_unencrypted.pdf'

                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        result_pdf = open(os.path.abspath(os.path.join(root, unencrypted_pdf_name)), 'wb')
                        pdf_writer.write(result_pdf)
                        print(f'Unencrypted {unencrypted_pdf_name}')
                        result_pdf.close()
                        pdf_file.close()
                    except PyPDF2.utils.PdfReadError:
                        print(f'Password for {file} is incorrect')
                        continue


def main():
    """
    Retrieves command line args
    :return: None
    """
    if len(sys.argv) > 2:
        folder_path = sys.argv[2]
        password = sys.argv[3]
        if sys.argv[1] == 'encrypt':
            encrypt(folder_path, password)
        elif sys.argv[1] == 'decrypt':
            decrypt(folder_path, password)
        else:
            print('usage: python pdf_paranoia {encrypt or decrypt} {folder_name} {password}')


if __name__ == '__main__':
    main()
