// genderChange
resultGen = document.getElementById('resultGen');
if (resultGen.textContent == "0"){
    // console.log(resultGen)
    resultGen.textContent = '男性';
}else{
    resultGen.textContent = '女性';
}

// ClassChange
resultCla =  document.getElementById('resultCla');
// console.log(resultCla);
if (resultCla.textContent == "1"){
    resultCla.textContent = "First-class";
} else if(resultCla == "2"){
    resultCla.textContent = "Second-class";
} else {
    resultCla.textContent = "Third-class";
}