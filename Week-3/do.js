// $(document).ready(function(){
//      addListenerToAddTask();

// });
// function addListenerToAddTask(){
//     $(".add-task").click(function(){
//         var valueTask = $(".input-task").val();
//         if(!valueTask){
//             alert("Please, enter your text")
//             return false
//         }
//         var containerTodo = "<div class = 'todo-container'>" + valueTask + "<button class='dlt-btn'>X</button></div>";
//         $(".todos-container").append(containerTodo);
//         $(".input-task").val("");
//     });
// }
const input = document.getElementById('input');
const btn = document.getElementById('btn');
const list = document.getElementById('list');

let id = 0;

function addElement(toDo, id) {
    const text = `<li class="list__item">
                    <input type="checkbox" class="checkbox" id="${id}" job="complete">
                    <label class="label"> ${toDo}</label>
                    <span class="delete-icon" job="delete" id="${id}"></span>
                </li>`
    const position = 'afterend'
    list.insertAdjacentHTML(position, text);
}

function completeToDo(element) {
    element.parentNode.querySelector('.label').classList.toggle('line');
}

function removeToDo(element) {
    element.parentNode.parentNode.removeChild(element.parentNode);
}


function pressBtn() {
    const toDo = input.value;
    if(toDo) {
        addElement(toDo, id);
        id++;
     }else {
        addElement(toDo, id);
        id++;
         //alert('Input is empty');
     }
     input.value = '';
}

list.addEventListener('click', function(event){
    console.log('OK');
    let element = event.target;
    const elementJOB = event.target.attributes.job.value;
    if(elementJOB == 'complete') {
        completeToDo(element);
    }else if (elementJOB == 'delete') {
        removeToDo(element);
    }
});
