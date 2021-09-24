from tool_dir.BidiHandler import BidiHandler

def demo():
	test_para = '''ãËÇá ááßÊÇÈÉ ÇáÚÑÈíÉ ÇáãÎÊáØÉ ÈÇáÜ English áÊÌÑÈÉ Çá BidiHandler.
ÇáÃÏÇÉ ãäÇÓÈÉ ááÌãá ÇáãÎÊáØÉ ááÛÊíä with two different directionalities.
ãËÇá Úáì Ğáß ÚäÏ ßÊÇÈÉ ßáãÉ ÅäÌáíÒíÉ æÓØ äÕ ÚÑÈí. ãËÇá:
ÚäÏ ßÊÇÈÉ Ó + Õ = x + y in English.
'''
	test = BidiHandler.Bidi(test_para)

	return test.RightToLeftEmbedding()
	