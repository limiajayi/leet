var isValid = function (s) {
    var chars = "({[";
    var arr = s.split("");
    var stack = [];
    var value = false;
    for (var i = 0; i < s.length; i++) {
        if (chars.indexOf(arr[i]) !== -1) {
            stack.push(arr[i]);
        }
        else {
            console.log(stack);
            switch (arr[i]) {
                case ")":
                    value = stack.pop() === '(' ? true : false;
                    stack.pop();
                    break;
                case "]":
                    value = stack.pop() === '[' ? true : false;
                    stack.pop();
                    break;
                case "}":
                    value = stack.pop() === '{' ? true : false;
                    stack.pop();
                    break;
                default:
                    break;
            }
        }
    }
    return value;
};
console.log(isValid("([])"));
