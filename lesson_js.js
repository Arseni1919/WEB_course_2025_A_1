// console.log('Hello, World!')
// console.error('This is ERROR!!!!!!')
// console.warn('This is Warning!!!!!!')
// console.info('This is INFO')

// let and const

// let age = 30
// age = 31
// console.log(age)
//
// const age2 = 31
// console.log(age2)

// variables

// const name = 'John'
// const age = 30
// const rating = 4.5
// const isCool = true
// let x = null
// const y = undefined
// let z
//
// console.log(typeof z)

// operators

// let x = 4
// let y = 5
// x += y
// console.log(x)
// x %= y
// console.log(x)
// x **= y
// console.log(x)


// concat

// const name = 'Ariel'
// const age = 20
//
// console.log('My name is ' + name + ' and I am ' + age)
// console.log("My brother's name is " + name + " and I am " + age)
// console.log("My brother's name is " + '"' + name + '"' + " and I am " + age)
// console.log(`My brother's name is "${name}" and I am ${age}`)


// strings

// const s = 'Hello, World!'
// console.log(s.length)
// console.log(s.toLowerCase())
// console.log(s.toUpperCase())
// console.log(s.substring(0, 7))
// console.log(s.substring(0, 5).toUpperCase())
// console.log(s.split(', '))


// arrays

// const numbers = new Array(1, 2, 3, 4)
// console.log(numbers)


// const numbers = [1, 2, 3, 4]
// console.log(numbers)


// const numbers = [1, 'string', 3.5, true]
// console.log(numbers)
// console.log(numbers[2])


// const fruits = ['apple', 'orange', 'banana']
// // fruits[5] = 'grapes'
// fruits.push('grapes')
// fruits.unshift('mango')
// console.log(fruits)
// fruits.pop()
// console.log(fruits)
// console.log(Array.isArray(fruits))
// console.log(fruits.indexOf('banana'))


// object literals

const person = {
    firstName: 'John',
    lastName: 'Doe',
    age: 30,
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: '50 main st',
        city: 'Boston',
        state: 'MA'
    }
}

// console.log(person)
// console.log(person.firstName)
// console.log(person.address.city)

// const {firstName, lastName, address: {city}} = person
// console.log(firstName)
// console.log(lastName)
// console.log(city)

// person.email = 'john@gmail.com'
// console.log(person)

const todos = [
    {
        id: 1,
        text: 'do homework',
        isCompleted: true
    },
        {
        id: 2,
        text: 'do dishes',
        isCompleted: true
    },
        {
        id: 3,
        text: 'meeting',
        isCompleted: false
    },
]

// console.log(todos)
// console.log(todos[1])


// json

// const todosJSON = JSON.stringify(todos)
// console.log(todosJSON)
// console.log( typeof todosJSON)

// const backToObjectTodos = JSON.parse(todosJSON)
// console.log(backToObjectTodos)
// console.log( typeof backToObjectTodos)

// loops

// for(let i = 0; i < 10; i++){
//     console.log(`index: ${i}`)
// }
//
// let i = 0
// while(i < 10){
//     console.log(`index: ${i}`)
//     i++
// }

// for(let i = 0; i < todos.length; i++){
//     console.log(todos[i].text)
// }
//
// for(let todo of todos){
//     console.log(todo.text)
// }

// todos.forEach(
//         function (todo) {
//             console.log(todo.text)
//         }
// )
//
//
// const texts = todos.map(
//         function (todo) {
//             // do something here
//             return todo.text.toUpperCase()
//         }
// )
// console.log(texts)
//
//
// const completedTasks = todos.filter(
//         function (todo) {
//             return todo.isCompleted
//         }
// ).map(
//         function (todo) {
//             return todo.text
//         }
// )
// console.log(completedTasks)


// conditionals

// const x = '10'
// const y = 10
// console.log(x === y)

// const x = true
// const y = false
// console.log(x || y)
// console.log(x && y)
//
// if (x > -5 || y > 10){
//     console.log('yes!')
// } else {
//     console.log('no!')
// }

// const x = 10
// const color = x > 10 ? 'red': 'blue'
// console.log(color)


// const color = 'red'
//
// switch (color) {
//     case 'red':
//         console.log('color is red')
//         break
//     case 'blue':
//         console.log('color is blue')
//         break
//     default:
//         console.log('color is other')
//         break
// }


// functions


// function addNums1(num1, num2) {
//     console.log(num1 + num2)
// }
// addNums1(10, 12)
//
//
// function addNums2(num1, num2) {
//     return num1 + num2
// }
// console.log(addNums2(10, 12))
//
//
// function addNums3(num1=1, num2=2) {
//     return num1 + num2
// }
// console.log(addNums3())


// arrow functions

// function addOne(num1) {
//     return num1 + 1
// }

// const addOne = num1 => num1 + 1
// console.log(addOne(2))
// const addNums = (num1, num2) => num1 + num2
// console.log(addNums(2, 3))

// const addNums = (num1=1, num2=2) => {
//     console.log('Inside arrow function')
//     return num1 + num2
// }
// console.log(addNums())
//
// todos.forEach(todo => console.log(todo.text))
// const texts = todos.map(todo => todo.text)
// const completed = todos.filter(todo => todo.isCompleted).map(todo => todo.text)
// console.log(completed)
















