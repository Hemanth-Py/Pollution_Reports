# Copyright (c) 2021 CodeOps Technologies LLP. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#   - Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   - Neither the name of CodeOps or the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# write the purpose of this code here
# Through this we are generating the pollution reports from XLSX file to
# a PDF in which the data is sorted by city wise pollution report and pollutant
# wise report of india

from PDFReport import PDFReport


def generate_city_pollution_report():  # file
    city_report.set_page_title_in_pdf(city_file, page_title='India Pollution Report - City-wise')
    city_report.add_report_generated_date(city_file, pollution_entries)
    city_report.create_table_with_heading(city_file, group_city_data, ['Avg', 'Max', 'Min', 'Pollutants'])
    city_report.save_file(city_file, 'CityWiseReport.pdf')


def generate_pollutants_wise_report():  # file
    pollutant_report.set_page_title_in_pdf(pollutant_file, page_title='India Pollution Report - Pollutants-wise')
    pollutant_report.add_report_generated_date(pollutant_file, pollution_entries)
    pollutant_report.create_table_with_heading(pollutant_file, group_pollutant_data, ['Avg', 'Max', 'Min', 'City'])
    pollutant_report.save_file(pollutant_file, 'PollutantWiseReport.pdf')


if __name__ == '__main__':
    city_report = PDFReport()
    pollution_entries = city_report.read_data_and_clean('AirQuality-India-Realtime.xlsx')
    group_city_data = city_report.grouping_cols(pollution_entries, ['Country', 'State', 'City', 'Place'])
    city_file = city_report.create_pdf_and_add_page()
    generate_city_pollution_report()

    pollutant_report = PDFReport()
    pollution_entries = pollutant_report.read_data_and_clean('AirQuality-India-Realtime.xlsx')
    group_pollutant_data = pollutant_report.grouping_cols(pollution_entries, ['Pollutants', 'State'])
    pollutant_file = pollutant_report.create_pdf_and_add_page()
    generate_pollutants_wise_report()
