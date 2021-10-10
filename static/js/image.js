const copyBtn = [...document.getElementsByClassName('copy-btn')]

copyBtn.forEach(btn => btn.addEventListener('click', ()=>{
    const url = btn.getAttribute('data-url')
    console.log(url)
    navigator.clipboard.writeText(url)
    btn.textContent = 'copied'
}))