#include <iostream>
#include <string>

using namespace std;

int indexof(string s, char x){
    for (int i = 0 ; i < s.size(); i++){
        if (s[i] == x)
            return i;
    }
    return -1;
}

int main(){
    setlocale(LC_ALL, "ru-RU");

    string search;
    cout << "Ведите строку для перевода:\n";
    cin >> search;

    string eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,.";
    const char* rus[35] = { "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ",
                            "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э",
                            "я", "ч", "с", "м", "и", "т", "ь", "б", "ю" };

    string answer;
    for (int i = 0 ; i < search.size() ; i++){
        answer += rus[indexof(eng, search[i])];
    }

    cout << answer << "\n";

    return 0;
}