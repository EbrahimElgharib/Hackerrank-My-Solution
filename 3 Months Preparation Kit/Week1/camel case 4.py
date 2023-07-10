# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

while True:
    try:
        # get text line
        text_line = input().rstrip()

        # split text
        line_list = text_line.split(';')

        # check split S or Connect C
        if line_list[0] == 'S': # split
            
            result = line_list[2][0] # put first letter

            if line_list[1] == 'M': # method
                name = line_list[2][1:-2]
                print("name as M:", name)
            else: name = line_list[2][1:]
            # for M, C, V
            for n in name:
                print("n:", n)
                if n.isupper(): result += ' '
                result += n  
            
            print(result.lower())
            
        else:
            words_list = line_list[2].split(' ')
            
            print("Hi ", words_list) # test
            
            words_camelcase = list(map(str.title, words_list))
            
            print("Hi ", words_camelcase) # test
            
            if line_list[1] != 'C': # method or var
                words_camelcase[0] = words_camelcase[0].lower()

                if line_list[1] == 'M':
                    words_camelcase[-1] = words_camelcase[-1] + '()'
            
            print(''.join(words_camelcase))
    
    except EOFError:
        break

    
