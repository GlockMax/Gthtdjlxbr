using System;
using System.Diagnostics;

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
            
            Stopwatch sw = new Stopwatch();
            sw.Start();
            
            char[] eng = Convert.ToString("`1234567890-=\\qwertyuiop[]asdfghjkl;\'zxcvbnm,./ " +
                                          "~!@#$%^&*()_+|QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?").ToCharArray();
            char[] rus = Convert.ToString("ё1234567890-=\\йцукенгшщзхъфывапролджэячсмитьбю. " +
                                          "Ё!\"№;%:?*()_+/ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,").ToCharArray();
            
            string answer = "";
            for (int i = 0; i < search.Length; i++)
            {
                answer += rus[IndexOf(eng, search[i])];
            }
            
            Console.WriteLine(answer);
            sw.Stop();
            Console.WriteLine(sw.Elapsed);
        }
    }
}