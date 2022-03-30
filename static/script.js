let snippets = document.querySelectorAll('.snippet');
let innerhtml = '';
snippets.forEach((snippet) => {
    innerhtml = snippet.innerHTML;
    snippet.innerHTML = '';
    snippet.innerText = innerhtml;
});
const textarea = document.querySelector('#text-area');
const mail_info = document.querySelector('.mail-info');

textarea.addEventListener('keyup', (e) => {
    let emails = e.target.value.split(',').filter(d => d != '');
    mail_info.innerHTML = '';
    emails.forEach((email) => {
        mail_info.innerHTML += `<div class="mail">${email}</div>`;
    })
})

const keysubmit = document.getElementById('keysubmit');
keysubmit.addEventListener('submit', (e) => {
    e.preventDefault()
    let formdata = new FormData;
    let projectname = document.getElementsByName('projectname')[0].value;
    emails = keysubmit.querySelector('textarea').value;
    keysubmit.querySelector('textarea').value = '';
    let valid = checkvalid(emails)
    console.log(valid);
    if (valid === true) {
        formdata.append('emails', emails);
        formdata.append('projectname', projectname);
        formdata.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);

        mail_info.innerHTML = `
        <div class="spinner-border mt-2" role="status">
             <span class="visually-hidden">Loading...</span>
        </div>
        `
        fetch('', {
            method: 'POST',
            credentials: 'same-origin',
            body: formdata,
        }).then(data => data.json()).then(data => {
            document.getElementById('msg').innerText = '';
            mail_info.innerHTML = `
                        <div class="mt-2">
                        <h4>Your key is:</h4>
                        <div class='snippet'>${data.key}</div>
                        </div>
                        `
        })
    } else {
        document.getElementById('msg').innerText = 'Invalid email';
        let mails = document.querySelectorAll('.mail');
        valid.forEach(i => {
            mails[i].style.border = '3px solid red';
        })
    }
})

function checkvalid(emails) {
    emails = emails.split(',')
    let result = []
    emails.forEach((email, i) => {
        if (email.includes('@') && email.includes('.com')) {

        } else {
            result.push(i)
        }
    })
    if (result[0] == undefined) return true;
    return result;
}