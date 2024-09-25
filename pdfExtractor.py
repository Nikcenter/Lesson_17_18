import pdfx
import re
from pprint import pprint

def parse_pdf(pdfFile, regexStrings, region):
    relation = {}
    pdf = pdfx.PDFx(pdfFile)
    text = pdf.get_text()
    for i in range(len(regexStrings)):
        try:
            # Find all matches in loop
            regex = re.compile(regexStrings[i][1], re.DOTALL|re.MULTILINE)
            regexVar = regex.search(text)
            stringStripN = regexVar.group(regexStrings[i][2]).strip('\n') #removing paragraphs
            replaceS = stringStripN.replace('\n', ' ') #replacing remaining paragraphs with spaces
            print(replaceS)
            if regexStrings[i] == regexStrings[2]: #if parsing place adding region string to place, if not skip this
                relation[regexStrings[i][0]] = region + ' ' + replaceS
            else:
                relation[regexStrings[i][0]] = replaceS
        except AttributeError:
            print(f'Дані відсутні {pdfFile}')
            relation[regexStrings[i][0]] = 'Дані відсутні'
    pprint(relation)


def regex_strings(directory, region):
    print(directory)
    print(region)
    regexStrings = [["number", "(\d{10}:\d{2}:\d{3}:\d{4})", 0],  # parse number of plot
                    ["area", f"(Площа.*ділянки.*Місце розташування)(.*)(\n\d+[\.]?\d*\n)({region})", 3],
                    ["place", "(область.{1,90}рад[и|а])", 0],  # parse place
                    ["price", "(Значення, гривень\n)(.*)(\n\d{3,}[\.]\d+)", 3],  # parse price
                    ['name_owner',
                     '(Прізвище.* фізичної)(.*)(\n[А-ЩЬЮЯЇІЄҐ]\w+[-]*\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\n)', 3],
                    ['company_owner', '(права власності.+)(\n+.*\n+.+)(\n+)(.+юрид.+)(\n+)(.+)(\n|\s)(.+)', 8],
                    ['date_register', '(Дата державної.*)(\n\n\d\d\.\d\d\.\d{4})', 2],  # parse date of register
                    ['rent_company', '(право оренди земельної ділянки)(\n*)(.+)(\"|\»)(\n)', 3],  # parse rent company
                    ['rent_person',
                     '(право оренди земельної ділянки)(\n*[А-ЩЬЮЯЇІЄҐ]\w+[-]*\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\n*)',
                     2]]
    # Get all the PDF filenames.
    pdfFile = 'info_by_4820982400_07_000_0721.pdf'
    parse_pdf(pdfFile, regexStrings, region)
    print('Готово!')

regex_strings('.', 'Миколаївська')
