/**
 *  Abril 15, 2024 
 * directions is an arrayy of strings, and needs to be reversed
 * strategy create to vars that increment(left+) and decrement(right-)
 * Then you will swaps the positions. Simple enough  
 * */

function reverseTrail(directions) {
    
    let left = 0;
    let right = directions.length-1;
    let tmp_string = "";

    while(left < right){

        tmp_string = directions[left];
        directions[left] = directions[right];
        directions[right] = tmp_string;

        left++;
        right--;

    }

    return directions;

}


/**
 * Create a function named craftWoodSign that receives a string signText and a number borderWidth.

The function will create a wooden sign with the signText engraved in the center, surrounded by a border made of asterisks (*). 
The borderWidth determines the thickness of the border.

Here are the steps:
Reverse the signText.
Calculate the total width of the sign by adding the length of the signText and twice the borderWidth.
Create the top and bottom borders by repeating the asterisk character (*) for the total width of the sign.
Create the side borders by repeating the space character for borderWidth times, then adding the reversed signText, 
and finally repeating the space character for borderWidth times again.
Construct the final sign by concatenating the top border, the side borders, and the bottom border.
Return the completed wooden sign as a string.
 */


function craftWoodSign(signText, borderWidth) {
    
    const reversedText = signText.split('').reverse().join('');
    const totalWidth = signText.length + (2 * borderWidth);

    const topBottomBorder = '*'.repeat(totalWidth);
    const sideBorder = ' '.repeat(borderWidth) + reversedText + ' '.repeat(borderWidth);

    const woodenSign = topBottomBorder + '' + sideBorder + '' + topBottomBorder;
    return woodenSign;

}