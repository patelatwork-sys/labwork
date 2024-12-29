from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult, AnalyzeDocumentRequest

# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
endpoint = "https://di-poc-rk.cognitiveservices.azure.com/"
key = ""

# helper functions

def get_words(page, line):
    result = []
    if page.words:
        for word in page.words:
            if _in_span(word, line.spans):
                result.append(word)
    return result

def _in_span(word, spans):
    for span in spans:
        if word.span.offset >= span.offset and (
            word.span.offset + word.span.length
        ) <= (span.offset + span.length):
            return True
    return False

def analyze_layout():
    # sample document
    formUrl = "https://img1.wsimg.com/blobby/go/7b9328c0-c06d-4f43-959f-6e1ab36f906a/downloads/1cd5snj8i_373361.pdf"

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-layout", AnalyzeDocumentRequest(url_source=formUrl)
    )
    result: AnalyzeResult = poller.result()

    status = poller.status()
    if status == "succeeded":
        print("Test complete: Analysis was successful.")
        generate_markup(result)
    else:
        print("Test failed: Analysis was not successful.")
    print(f"Status: {status}")

def generate_markup(result: AnalyzeResult):
    with open("output.html", "w", encoding="utf-8") as file:
        file.write("<html><body>\n")
        file.write("<h1>Document Analysis Result</h1>\n")
        
        if result.pages:
            for page in result.pages:
                file.write(f"<h2>Page {page.page_number}</h2>\n")
                file.write("<h3>Lines</h3>\n")
                if page.lines:
                    for line in page.lines:
                        file.write(f"<p>{line.content}</p>\n")
                
                file.write("<h3>Words</h3>\n")
                if page.words:
                    for word in page.words:
                        file.write(f"<span>{word.content} </span>\n")
                
                if hasattr(page, 'tables') and page.tables:
                    file.write("<h3>Tables</h3>\n")
                    for table in page.tables:
                        file.write("<table border='1'>\n")
                        for cell in table.cells:
                            file.write(f"<tr><td>{cell.content}</td></tr>\n")
                        file.write("</table>\n")
        
        file.write("</body></html>\n")

if __name__ == "__main__":
    analyze_layout()