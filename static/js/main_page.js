window.onload = function(){
var state = document.getElementById("state");
var category = document.getElementById("category")

if (state.innerHTML == "UD") {
    state.innerHTML = "Used";
} 
else {
    state.innerHTML = "New"
}
    
switch (category.innerHTML){
    case "MOB":
        category.innerHTML = "Mobile Phones";
        break;
    case "COM":
         category.innerHTML = "Computers";
        break;
    case "MBA":
         category.innerHTML = "Mobile Accessories";
        break;
        case "CMA":
         category.innerHTML = "Computer Accessories";
        break;
    case "O":
         category.innerHTML = "Other";
                
}
}

