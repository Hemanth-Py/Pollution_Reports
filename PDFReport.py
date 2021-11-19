import pandas as pd
from fpdf import FPDF

PAGE_ORIENTATION_PORTRAIT = 'P'
A4_SIZE = 'A4'
HEIGHT = 10
WIDTH = 35
CENTER_ALIGN = "C"
FONT_STYLE_TIMES = 'Times'
FONT_SIZE_30 = 30
FONT_SIZE_20 = 20
FONT_SIZE_15 = 15
FONT_SIZE_10 = 10

# this class creates a DataFrame and groups the data.
# then its creates a report(pdf file) for grouped data


class PDFReport:

    def read_data_and_clean(self, xl_file):
        # reading excel file
        xl_data = pd.read_excel(xl_file)
        # dropping/removing empty rows
        xl_data.dropna(inplace=True)
        return xl_data

    def set_page_title_in_pdf(self, pdf_file, page_title):
        # font and size of the page heading
        pdf_file.set_font(FONT_STYLE_TIMES, size=FONT_SIZE_30)
        pdf_file.write(h=HEIGHT, txt=page_title + '\n')

    def add_report_generated_date(self, pdf_file, xl_data):
        # generated date to add it to the report
        day = ' '.join(xl_data['Lastupdate'].unique())
        generated_on_day = 'Generated on :' + day + '\n'
        pdf_file.set_font(FONT_STYLE_TIMES, size=FONT_SIZE_20)
        pdf_file.write(h=HEIGHT, txt=generated_on_day)
        # h = height, txt = text to print

    def create_pdf_and_add_page(self):
        # creating a file and adding a page to it
        pdf_file = FPDF(PAGE_ORIENTATION_PORTRAIT, format=A4_SIZE)
        pdf_file.add_page()
        return pdf_file

    def grouping_cols(self, xl_data, gp_cols_list):
        # grouping the columns
        gp_data = xl_data.groupby(gp_cols_list)
        return gp_data

    def create_table_with_heading(self, pdf_file, gp_data, table_cols):
        # looping through the grouped data
        for table_data in gp_data:  # create_table_with_heading
            # In table_data we get tuple of grouped columns and str of table

            # creating heading for the table
            self.create_heading_for_table(pdf_file, table_data)

            # table_cols = ['Avg','Max','Min','Pollutants']
            # filtering the columns according to requirement
            # and breaking the table into rows
            table = table_data[1].filter(items=table_cols).to_string(index=False).split('\n')

            self.create_table(pdf_file, table, table_cols)

    def create_heading_for_table(self, pdf_file, table_data):
        table_heading = ' - '.join(table_data[0])
        pdf_file.set_font(FONT_STYLE_TIMES, size=FONT_SIZE_15)
        pdf_file.write(h=HEIGHT, txt=table_heading + '\n')

    def create_table(self, pdf_file, table, table_cols):
        # font for the table
        pdf_file.set_font(FONT_STYLE_TIMES, size=FONT_SIZE_10)
        # iterating through rows and columns
        for row in table:  # create_table
            for col in range(len(table_cols)):
                self.breaking_row_into_columns_and_print(col, pdf_file, row, table_cols)
            self.insert_new_line_in_table_of_height_10(pdf_file)
        self.insert_new_line_in_table_of_height_10(pdf_file)

    @staticmethod
    def breaking_row_into_columns_and_print(col, pdf_file, row, table_cols):
        # why are doing this step of col < len(....
        # table_cols = ['Avg','Max','Min','Pollutants']
        # col = 0 to 3 , len(table_cols)=4
        # 1) row.split() --> [70.0, 108.0, 42.0, PM2.5]
        # 2) row.split() -->[21.0, 22.0, 19.0, Mandi, Gobindgarh]
        # In last iteration(means no.of cols-1) we have to take all elements as one item
        row_item = row.split()[col] if col < len(table_cols) - 1 else ' '.join(row.split()[col:])
        pdf_file.cell(w=WIDTH, h=HEIGHT, txt=row_item, align=CENTER_ALIGN, border=1)

    @staticmethod
    def insert_new_line_in_table_of_height_10(pdf_file):
        pdf_file.write(h=HEIGHT, txt='\n')

    @staticmethod
    def save_file(pdf_file, filename):
        pdf_file.output(filename)
