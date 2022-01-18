import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
text = r'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
print(tool.correct(text))
tool.close()