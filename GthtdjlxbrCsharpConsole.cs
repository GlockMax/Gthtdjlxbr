using System;

namespace Gthtdjlxbr
{
    static class Gthtdjlxbr
    {
        static int IndexOf(char[] A, char x) {
            for (int i = 0; i < A.Length; i++) {
                if (A[i] == x) {
                    return i;
                }
            }
            return -1;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Введите строку для перевода:");
            string search = Convert.ToString(Console.ReadLine());
            
            char[] eng = Convert.ToString("`1234567890-=\\qwertyuiop[]asdfghjkl;\'zxcvbnm,./ " +
                                          "~!@#$%^&*()_+|QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?").ToCharArray();
            char[] rus = Convert.ToString("ё1234567890-=\\йцукенгшщзхъфывапролджэячсмитьбю. " +
                                          "Ё!\"№;%:?*()_+/ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,").ToCharArray();
            
            string answer = "";
            for (int i = 0; i < search.Length; i++)
            {
                answer += IndexOf(eng, search[i]) != -1 ? rus[IndexOf(eng, search[i])] : search[i];
            }
            
            Console.WriteLine(answer);
        }
    }
}
