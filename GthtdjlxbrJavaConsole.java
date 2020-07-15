import java.util.*;

public class GthtdjlxbrJavaConsole
{
   /* public static HashMap <Character, Character> createDictOfChars(String keys, String values)
    {
        HashMap <Character, Character> eng = new HashMap <Character, Character> ();
        for ( int i = 0 ; i < keys.length() ; i++ ){
            eng.put(keys.charAt(i), values.charAt(i));
        }
        return eng;
    }*/

//=======================================================
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
        
        long startTime = System.currentTimeMillis() ;
	
        char[] eng = ( (String) "`1234567890-=\\qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+|QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?" ).toCharArray() ;
        char[] rus = ( (String) "ё1234567890-=\\йцукенгшщзхъфывапролджэячсмитьбю.Ё!\"№;%:?*()_+/ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ," ).toCharArray() ;

        String answer = "" ;
        
        for ( int i = 0 ; i < search.length() ; i++ )
        {
            answer += rus[IndexOf(eng, search.charAt(i))] ;
        }
        
        long timeSpent = System.currentTimeMillis() - startTime ;
        System.out.println(answer) ;
        System.out.println("Время выполнения: " + timeSpent / 1000.0  + " секунд") ;
    }
}
