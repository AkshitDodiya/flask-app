
try :
    from run import app
    import unittest
    
except Exception as e :
    print(f"Some module are missing : {e}")

class FlaskTest(unittest.TestCase):
    
    #check for response 200
    def test_index(self) :
        tester = app.test_client(self)
        response = tester.get('/')
        status = response.status_code
        self.assertEqual(status,201)    
        
if __name__ == "__main__":
    unittest.main()