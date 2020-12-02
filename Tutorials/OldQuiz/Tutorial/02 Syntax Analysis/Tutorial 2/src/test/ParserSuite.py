import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """int a, b, c;
        float foo(int a; float c, d) {
            int e;
            e = a + 4;
            c = a * d / 2.0;
            return c + 1;
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_4(self):
        input = """
                float a, d ;
                int function1(){
	               int b,c,e,k;
	               e = a + b - c * d / (k-1) ;
	               x = (2-1) ;
	               return x;
                }

                float function2(int x, y){
	               float k;
	               k = (1-2)*2*3*(4-function1());
	               a = 1 * 2 * 3 * (function1()*2);
	               return k ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204)) ;
        
    def test_5(self):
        input = """
                float fast_read()
                {
                    sync_with_stdio(false);
                    tie(0);
                }

                int main()
                {
                    int a, b;
                    int ans;
                    ans = 1e18;
                    int t;
                    t = 1e18;
                    fast_read();
                    input(a, b);
                    output(ans);
                    return 0;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205)) ;
    
    def test_6(self):
        input = """
                int main(){
                    ios::sync_with_stdio(false);
                    cin>>a>>b;
                    ll x = a, y = b;
                    ll ans = 1e18;
                    for (ll i=1;i*i<=(a + b);i++) {
                        if (a%i==0)
                            x = a/i;
                        if (b%i==0)
                            y = b/i;
                        if ((a+b)%i==0) {
                            ll v = (a+b)/i;
                            if (v>=x||v>=y) {//
                                ans = min(ans,v+v+i+i);
                            }
                        }
                    }
                    cout<<ans;
                }
                """
        expect = "Error on line 3 col 23: :"
        self.assertTrue(TestParser.test(input,expect,206)) ;