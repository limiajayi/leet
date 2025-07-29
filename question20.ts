const isValid = (s: string): boolean => {

    let chars: string = "({[";
    let arr: string[] = s.split("");
    let stack: string[] = [];
    let value: boolean = false


    for (let i = 0; i < s.length; i++) {
        if (chars.indexOf(arr[i]) !== -1) {
            stack.push(arr[i])
        } else {

            console.log(stack)
            switch (arr[i]) {
                
                case ")":
                    value = stack.pop() === '(' ? true : false; 
                    break;
                case "]":
                    value = stack.pop() === '[' ? true : false; 
                    break;
                case "}":
                    value = stack.pop() === '{' ? true : false; 
                    break;
                default:
                    break;

            }

            
        }
    }

    return value
};

console.log(isValid("([])"))