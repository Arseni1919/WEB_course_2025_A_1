// console.log('Lesson 2 of JS')

// Old Way to create Objects in JS


// function addOne(num){
//     // return num + 1
//     console.log(num + 1)
// }

// function Person(firstName, lastName, dob) {
//     this.firstName = firstName
//     this.lastName = lastName
//     // this.dob = dob
//     this.dob = new Date(dob)
//
//     // this.getBirthYear = function () {
//     //     return this.dob.getFullYear()
//     // }
//     //
//     // this.getFullName = function () {
//     //     return `My name is ${this.firstName} ${this.lastName}`
//     // }
// }


// const person1 = new Person('Moti', 'Katz', '4-3-1980')
// const person2 = new Person('Rina', 'Katz', '5-7-1988')

// console.log(person1)
// console.log(person2)

// console.log(person1.dob)
// console.log(person1.dob.getDay())
// console.log(person1.dob.getFullYear())


// Person.prototype.getBirthYear = function () {
//         return this.dob.getFullYear()
// }
//
// Person.prototype.getFullName = function () {
//         return `My name is ${this.firstName} ${this.lastName}`
// }


// console.log(person1.getBirthYear())
// console.log(person1.getFullName())


// New Way to create Objects in JS

// class Person {
//     constructor(firstName, lastName, dob) {
//         this.firstName = firstName
//         this.lastName = lastName
//         this.dob = new Date(dob)
//     }
//
//     getBirthYear() {
//         return this.dob.getFullYear()
//     }
//
//     getFullName() {
//         return `My name is ${this.firstName} ${this.lastName}`
//     }
// }
//
//
// const person1 = new Person('Moti', 'Katz', '4-3-1980')
// const person2 = new Person('Rina', 'Katz', '5-7-1988')
//
//
// console.log(person1.getBirthYear())
// console.log(person1.getFullName())


// Window


// console.log(window)
// alert('This is annoying message! Yayyyy!')
// console.log(window.innerHeight)
// console.log(window.innerWidth)
// console.log(window.localStorage)
// console.log(window.document)

// console.log(document.getElementById('my-form'))
// console.log(document.getElementsByClassName('block')[0])
// console.log(document.getElementsByTagName('form')[0])
//
// console.log(document.querySelector('#my-form'))
// console.log(document.querySelector('.block'))
// console.log(document.querySelector('form'))
//
// console.log(document.querySelectorAll('.item'))
// console.log(document.querySelectorAll('li'))

// const items = document.querySelectorAll('.item')
// items.forEach(item => console.log(item))

// Change DOM

// const ul = document.querySelector('.items')

// ul.remove()

// ul.firstElementChild.remove()
// ul.lastElementChild.remove()
// ul.children[3].remove()

// ul.firstElementChild.textContent = 'Hello!'
// ul.children[1].innerText = '<h2>Brad</h2>'
// ul.children[2].innerHTML = '<h2>Betty</h2>'
//
// const btn = document.querySelector('.btn')


// btn.addEventListener('click', (e) => {
//     e.preventDefault()
//     // console.log('click')
//     // console.log(e)
//     // console.log(e.target)
//     // console.log(e.target.className)
//     // document.querySelector('#my-form').style.background = '#ccc'
//     // document.querySelector('body').style.background = 'black'
//     // document.querySelector('body').style.color = 'white'
//     // document.querySelector('.items').lastElementChild.innerHTML = '<h1>CLICKED!</h1>'
//     // btn.style.background = 'red'
//     // btn.style.color = 'white'
//
// })


// btn.addEventListener('mouseover', (e) => {
//     e.preventDefault()
//     document.querySelector('body').classList.remove('white-bg')
//     document.querySelector('body').classList.add('black-bg')
// })
//
//
// btn.addEventListener('mouseout', (e) => {
//     e.preventDefault()
//     document.querySelector('body').classList.remove('black-bg')
//     document.querySelector('body').classList.add('white-bg')
// })

// btn.style.background = 'red'
// btn.style.color = 'white'


// Big Example


// const myForm = document.querySelector('.my-form')
// const nameInput = document.querySelector('#name')
// const emailInput = document.querySelector('#email')
// const msg = document.querySelector('.msg')
// const userList = document.querySelector('.users')
//
// const onSubmit = (e) => {
//     e.preventDefault()
//     if (nameInput.value === '' || emailInput.value === '') {
//         // alert('Fill all inputs!')
//         msg.innerHTML = 'Please enter all fields!'
//         msg.classList.add('error')
//         // setTimeout(() => {
//         //     msg.innerHTML = ''
//         //     msg.classList.remove('error')
//         // }, 1000)
//     } else {
//         const li = document.createElement('li')
//         li.innerText = `${nameInput.value}: ${emailInput.value}`
//         userList.appendChild(li)
//         nameInput.value = ''
//         emailInput.value = ''
//         msg.innerHTML = 'User Added!'
//         msg.classList.remove('error')
//         msg.classList.add('success')
//         setTimeout(() => {
//             msg.innerHTML = ''
//             msg.classList.remove('success')
//         }, 5000)
//     }
// }
//
// myForm.addEventListener('submit', onSubmit)




