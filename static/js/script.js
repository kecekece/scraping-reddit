let isSubmitting = false;
let commentCount = 0;
let hateCommentCount = 0;
let nonHateCommentCount = 0;

document.getElementById('form-url').addEventListener('submit', (event)=>{
    event.preventDefault();
    console.log(isSubmitting);
    

    if (isSubmitting) {
        Swal.fire({
            text: 'Harap tunggu sampai proses selesai...',
            icon: 'info',
        });
        return;
    }
    
    resetCountComment();
    resetCountCommentElement();
    toggleSubmitting();
    toggleLoader();
    document.querySelectorAll('tbody tr').forEach(elem => {
        elem.remove();
    })

    event.stopPropagation()
    urlInput = event.target.url.value;
    console.log(urlInput);

    axios.post('/', {
        url : urlInput,
    }).then((result) => {
        comments = result.data;

        const tableBody = document.querySelector('#data-scraping tbody');
        comments.forEach((comment, index) => {
            const row = document.createElement('tr');

            const tdAuthor = document.createElement('td');
            tdAuthor.textContent = comment.author;

            const tdComment = document.createElement('td');
            tdComment.textContent = comment.body;

            const tdLabel = document.createElement('td');
            const labelDivComment = document.createElement('div');
            if(comment.label == 0){
                nonHateCommentCount += 1;
                labelDivComment.textContent = 'Non-Hate Speech';
                labelDivComment.classList.add('label','non-hate-comment')
            } else if(comment.label == 1){
                hateCommentCount += 1;
                labelDivComment.textContent = 'Hate Speech';
                labelDivComment.classList.add('label','hate-comment')
            }
            tdLabel.appendChild(labelDivComment)

            row.appendChild(tdAuthor)
            row.appendChild(tdComment)
            row.appendChild(tdLabel)

            tableBody.appendChild(row)
        });

        commentCount = comments.length;
        document.getElementById('total-comment').innerText = commentCount;
        document.getElementById('hate-data').innerText = hateCommentCount;
        document.getElementById('non-hate-data').innerText = nonHateCommentCount;
    }).catch((err) => {
        if(err.response){
            Swal.fire({
                text: capitalizeFirstLetter(err.response.data.error),
                icon: 'error',
            });
        }
        console.log(err);
    }).finally(()=>{
        toggleSubmitting();
        toggleLoader();
    });
})


document.querySelector('.reset-btn').addEventListener('click', (e)=>{
    document.getElementById('form-url').reset();
    document.getElementById('url').focus();
});


function toggleLoader(){
    if(document.querySelector('.loading-container').style.display == 'flex'){
        document.querySelector('.loading-container').style.display = 'none'
    }else{
        document.querySelector('.loading-container').style.display = 'flex';
    }
}

function toggleSubmitting(){
    if(isSubmitting){
        isSubmitting = false;
    }else{
        isSubmitting = true;
    }
}

function capitalizeFirstLetter(str) {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1);
}


function resetCountComment(){
    hateCommentCount = 0;
    nonHateCommentCount = 0;
    commentCount = 0;
}

function resetCountCommentElement(){
    document.getElementById('total-comment').innerText = commentCount;
    document.getElementById('hate-data').innerText = hateCommentCount;
    document.getElementById('non-hate-data').innerText = nonHateCommentCount;
}