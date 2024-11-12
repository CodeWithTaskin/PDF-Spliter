from PyPDF2 import PdfWriter, PdfReader

class Configuration:
    def __init__(self):
        try:
            self.pdf_path = input("Enter your PDF path: ")
            self.splitting_type = input('Do you want "Full PDF Split" or "Specific Split"?\n[Type "full" or "specific: "]')
            self.chapter_name = input('Enter your chapter name: ')
            self.output_path = input('Enter path you want your output: ')
            if self.splitting_type == 'full'.lower():
                self.page_len = int(input("How many page you want in every chapter? "))
            elif self.splitting_type == 'specific'.lower():
                self.page = input("Witch page you want to split?\n[Type 1,5 or (1-10)]--> ")
                if '-' in self.page:
                    start= self.page.split('-')[0]
                    end = self.page.split('-')[-1]
                    self.list_of_page = list(range(int(start),int(end)+1))
                else:
                    self.list_of_page = {int(x) for x in self.page.split(',')}
        except ValueError:
            print('Please enter your information correctly.')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
                


class FullSplit:
    def full_split_proses(self,path,page_len,chapter_name):
        reader = PdfReader(path)
        start = 0
        end = page_len
        remaining = len(reader.pages)%page_len
        pdf_len = len(reader.pages) - remaining
        for page_num in range(int(pdf_len/page_len+1)):
            chapter = list(range(start,end))
            output = PdfWriter()
            for j in chapter:
                if j in chapter:
                    output.add_page(reader.pages[j])
                    with open(f"{chapter_name}{page_num}.pdf", "wb") as output_stream:
                        output.write(output_stream)
            start = end
            end = end + page_len
            if end > len(reader.pages):
                end = start + remaining
                
class SpecificSplit:
    def specific_split_proses(self,path,page_len,chapter_name):
        reader = PdfReader(path)
        output = PdfWriter()
        chapter = page_len
        for page_num in chapter:
            if page_num in chapter:
                output.add_page(reader.pages[page_num])
                with open(f"{chapter_name}.pdf", "wb") as output_stream:
                    output.write(output_stream)

con = Configuration()
FS = FullSplit()
SS = SpecificSplit()
