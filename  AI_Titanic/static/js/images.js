// GenderSelect
var pics_src = new Array("../../static/img/man.jpeg","../../static/img/woman.jpg");
var genderElement = document.getElementById("select1");
var gender = document.getElementById('gender');

genderElement.onchange = function(){
    gender.classList.add('transparent');
    setTimeout('timedisp(gender, pics_src, genderElement)', 250);
    setTimeout('timetrans(gender)', 500);
}

// ClassSelect
var grade_src = new Array(null, "../../static/img/firstclass.jpg","../../static/img/secondclass.jpg","../../static/img/thirdclass.jpeg")
var gradeElement = document.getElementById('select2');
var garce = document.getElementById('grade');

gradeElement.onchange = function(){
    grade.classList.add('transparent');
    setTimeout('timedisp(grade, grade_src, gradeElement)', 250);
    setTimeout('timetrans(grade)', 500);
    fareDisplay(gradeElement.value);
}

// 画像変更とfadeout
function timedisp(transer, images, element){
    transer.src=images[element.value];
}

function timetrans(transer){
    transer.classList.remove('transparent');
}

// fare表示
if (gradeElement){
    var fare = document.getElementsByClassName('fare');
    fareDisplay(gradeElement.value);
}
function fareDisplay(number){
    fare[0].classList.add('disNone');
    fare[1].classList.add('disNone');
    fare[2].classList.add('disNone');
    if (number == 1) {
        fare[0].classList.remove('disNone');
    }else if(number == 2){
        fare[1].classList.remove('disNone');
    }else if(number == 3){
        fare[2].classList.remove('disNone');
    }
}

// submitチェック
function checkSubmit() {
    var checkNum = gradeElement.value
    var price = document.getElementById('select3').value
    if(isNaN(price)){
        window.alert('数字を入れてください')
        return false;
    }
    if (checkNum == 1) {
        if(25<=price && price<=512){
            console.log(price);
            return true;
        }else{
            var miss = 1;
        }
    }else if(checkNum == 2){
        if(0<=price && price<=73.5){
            console.log(price);
            return true;
        }else{
            var miss = 1;
        }
    }else if(checkNum == 3){
        console.log(price);
        if(0<=price && price<=69.55){
            return true;
        }else{
            var miss = 1;
            console.log(miss);
        }
    }
    if(miss == 1){
        window.alert('range外です')
        return false;
    }
}