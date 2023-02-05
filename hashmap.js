people = ["Alice", "Bob", "Chris", "Dan"];
isFirstPhrase = true;
isFirstTime = true;

score = 0;

function hash(str){
    let num = 0;
    num = str[0].charCodeAt(0);
    console.log(str);
    console.log(num %4);
    return num % 4;
}

function randomElement(){
    let index = Math.floor((Math.random()*people.length));
    let person = people[index];
    people.splice(index, 1);
    console.log(people);
    return person;
}


function myMove() {
    if(isFirstPhrase){
        let person = randomElement();
        if(people.length == 0) isFirstPhrase = false;
        let id = null;
        const elem = document.getElementById("animate");
        elem.innerHTML = person;
        let pos = 146;
        clearInterval(id);
        id = setInterval(frame, 5);
        function frame() {
            if (pos == 500) {
                clearInterval(id);
            } else {
                // check if hash is produced
                if(pos == 350){
                    let elem = document.getElementById("animate");
                    hash_index = hash(person);
                    elem.innerHTML+=(", " + hash_index);
                }
                pos++;
                // elem.style.top = pos + 'px';
                elem.style.left = pos + 'px';
            }
        }
    } else {
        if (isFirstTime){
            people = ["Alice", "Bob", "Chris", "Dan"];
            isFirstTime = false;
            colors = ["blue", "red", "green", "purple"]
            // get array
            var  array= document.getElementById("array");
            console.log(array);
            for(let i = 0; i < 4; i++){
                var e = array.children[i];
                console.log( e.style.backgroundColor);
                e.style.color = colors[i];
            }
        }
        let person = randomElement();
        if(people.length == 0) isFirstPhrase = false;
        let id = null;
        const elem = document.getElementById("animate");
        elem.innerHTML = person;
        let pos = 146;
        clearInterval(id);
        id = setInterval(frame, 5);
        function frame() {
            if (pos == 500) {
                clearInterval(id);
            } else {
                // check if hash is produced
                if(pos == 350){
                    let elem = document.getElementById("animate");
                    hash_index = hash(person);
                    elem.innerHTML+=(", " + hash_index);
                }
                pos++;
                // elem.style.top = pos + 'px';
                elem.style.left = pos + 'px';
            }
        }
    }
    
}

function putElement(button){
    const elem = document.getElementById("animate");
    let div = button.parentElement;
    div.innerHTML = elem.innerHTML;
    if(people.length == 0) {
        window.alert("Phase 2");
    }
}

function checkAnswer(div){
    const elem = document.getElementById("animate");
    if(!isFirstPhrase){
        let text = div.innerHTML;
        if(text == elem.innerHTML){
            div.style.color = "white";
            score+=1;
            console.log(score);
            if(score > 4){
                text="Congrats, Next Level";
                document.write('<h1>'+text+'</h1>');
            }
        } else {
            text="Sorry Start Over";
            document.write('<h1>'+text+'</h1>');
            console.log("WRONG");
        }
    }
}