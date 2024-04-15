
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
 *  Abril 15, 2024 
 * directions is an arrayy of strings, and needs to be reversed
 * strategy create to vars that increment(left+) and decrement(right-)
 * Then you will swaps the positions. Simple enough  
 * */