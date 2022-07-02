
class number_to_roman:

    def convert(self, number):
        number_roman_map = {
        0:'로마자 0은 존재하지 않습니다.', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X'
    }

        def str_to_num(self, target_str):
            result = int(target_str)
            return result
    
        def matching_num(self, number):
            matched_num = number_roman_map[number]
            return matched_num
        
        if type(number) == str:
           converted_num = str_to_num(self, number)
           result_roman_num = matching_num(self, converted_num)
           return result_roman_num

        if type(number) == list:
            result_arr = []
            for target_num in number:
                result = matching_num(self, target_num)
                result_arr.append(result)
            return result_arr

        if type(number) == int:
            result_roman_num = matching_num(self, number)
            return result_roman_num
        
        return 'error!!'


        
