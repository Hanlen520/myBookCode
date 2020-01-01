import sys,unittest
sys.path.append('../common')
sys.path.append('../page')
from ownUnit import MyunitTests # ������Թؼ�������
from helper import Helper # ���� Helper ��
from time import sleep
from getImage import SaveImage # �����ͼ����
import logging # ������־ģ��

class TestLogin(MyunitTests,Helper):

 def testlogin(self):
	 ''' ��ȷ���û��������� '''
	 self.loginpage.openLoginPage()
	 self.log('PO-gjs ������������뵽��Ŀ��ҳ ')
	 self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
	 self.log('PO-gjs ��������ȷ���û��������� ')
	 self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1)) # ����
	 self.log('PO-gjs ����¼�ɹ���ȡ��Ϣ���ж��� ')
	 SaveImage(self.dr,'login_success.png')
	 self.log('PO-gjs ����¼�ɹ����ȡ��ͼ��Ϣ ')
	 self.log('PO-gjs ���� 4 ������ִ�н��� .....')
	 
 def test_user_null(self):
	 ''' ��������Ϊ�� '''
	 self.loginpage.openLoginPage()
	 self.log('PO-gjs ������������뵽��Ŀ��ҳ ')
	 self.loginpage.login_gjs_pro(self.readusername(2),self.readpassword(2))
	 self.log('PO-gjs ��������ȷ�û���������Ϊ�� ')
	 # ����
	 self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(2))
	 self.log('PO-gjs ����¼ʧ�ܻ�ȡ��Ϣ���ж��� ')
	 SaveImage(self.dr,'loginpasswdNull.png')
	 self.log('PO-gjs ����¼ʧ�ܺ��ȡ��ͼ��Ϣ ')
	 self.log('PO-gjs ���� 1 ������ִ�н��� .....')
	 
 def test_username_null(self):
	 ''' �����û���Ϊ�� '''
	 self.loginpage.openLoginPage()
	 self.log('PO-gjs ������������뵽��Ŀ��ҳ ')
	 self.loginpage.login_gjs_pro(self.readusername(3),self.readpassword(3))
	 self.log('PO-gjs �������û���Ϊ�պ���ȷ���� ')
	 self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(3))
	 self.log('PO-gjs ����¼ʧ�ܻ�ȡ��Ϣ���ж��� ')
	 SaveImage(self.dr,'loginuserNull.png')
	 self.log('PO-gjs ����¼ʧ�ܺ��ȡ��ͼ��Ϣ ')
	 self.log('PO-gjs ���� 3 ������ִ�н��� .....')
	 
 def test_user_passwd_null(self):
	 ''' �����û��� / ����Ϊ�� '''
	 self.loginpage.openLoginPage()
	 self.log('PO-gjs ������������뵽��Ŀ��ҳ ')
	 self.loginpage.login_gjs_pro(self.readusername(4),self.readpassword(4))
	 self.log('PO-gjs �������û���Ϊ�պ���ȷΪ�� ')
	 self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(4))
	 self.log('PO-gjs ����¼ʧ�ܻ�ȡ��Ϣ���ж��� ')
	 SaveImage(self.dr,'loginuserAndpasswd.png')
	 self.log('PO-gjs ����¼ʧ�ܺ��ȡ��ͼ��Ϣ ')
	 self.log('PO-gjs ���� 2 ������ִ�н��� .....')
	 
if __name__ == '__main__':
	unittest.main(verbosity=2)