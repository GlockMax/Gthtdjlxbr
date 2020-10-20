import java.util.*;

public class GthtdjlxbrJavaConsole
{
    public static int IndexOf (char arr[], char c)
    {
        for ( int i = 0 ; i < arr.length ; i++ )
	{
	    if ( arr[i] == c )
	    {
	        return i;
	    }
	}
	return -1;
    }
    
    public static void main (String args[])
    {
        Scanner scan = new Scanner(System.in) ;
        System.out.println("Введите строку для перевода ") ;
        String search = (String) scan.nextLine() ;
        
        char[] eng = ( (String) "`1234567890-=\\qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+|QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?" ).toCharArray() ;
        char[] rus = ( (String) "ё1234567890-=\\йцукенгшщзхъфывапролджэячсмитьбю.Ё!\"№;%:?*()_+/ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ," ).toCharArray() ;

        String answer = "" ;
        
        for ( int i = 0 ; i < search.length() ; i++ )
        {
            answer += IndexOf(eng, search.charAt(i)) != -1 ? rus[IndexOf(eng, search.charAt(i))] : search.charAt(i);
        }
        
        System.out.println(answer) ;
    }
}
