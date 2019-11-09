#! python3
# brute_force_pdf_breaker.py
# usage: python brute_force_pdf_breaker.py {pdf_file} {dictionary.txt}

import sys
import PyPDF2


def main():
    """
    Checks for inputs via sys.argv
    :return: Calls pdf_brute_force or prints usage statement.
    """
    if len(sys.argv) > 2:
        pdf_file = sys.argv[1]
        dictionary_file = sys.argv[2]
        pdf_brute_force(pdf_file, dictionary_file)

    else:
        print('usage: python brute_force_pdf_breaker.py {pdf_file} {dictionary.txt}')


def pdf_brute_force(pdf_file, dictionary_file):
    """
    :param pdf_file: path of pdf file to be decrypted
    :param dictionary_file: path of dictionary file
    :return: exits if file is not encrypted or cannot be decrypted, else returns password used to decrypt
    """
    pdf = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))

    # check for encrypted pdf, if not, prints and exits
    if not pdf.isEncrypted:
        print('File is not encrypted')
    else:
        # opens dictionary file, reads it, splits into list of words
        dictionary = open(dictionary_file, 'r').read().split('\n')

        # iterates through dictionary and tries passwords, 1 if match, exits if password is found
        for word in dictionary:
            print(word)
            if pdf.decrypt(word) == 1 or pdf.decrypt(word.lower()) == 1:
                print(f'Password is {word}')
                return word
        print('No password match found.')


if __name__ == '__main__':
    main()
