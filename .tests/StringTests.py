import main


def testContains():
    text = 'dwaoijng agfjanwgaw g awjg awjg awjg awjg ajg jawg awjg awihgb awuigb aw abc'
    assert main.text_contains_word(text, 'abc') == True
    assert main.text_contains_word(text, '8745') == False
