from tool_dir.BidiHandler import BidiHandler

def demo():
	test_para = '''���� ������� ������� �������� ���� English ������ �� BidiHandler.
������ ������ ����� �������� ������ with two different directionalities.
���� ��� ��� ��� ����� ���� �������� ��� �� ����. ����:
��� ����� � + � = x + y in English.
'''
	test = BidiHandler.Bidi(test_para)

	return test.RightToLeftEmbedding()
	