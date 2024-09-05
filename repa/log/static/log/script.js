var popup

const save_changes = async () => {
	lessons = document.querySelectorAll('.checkbox')
	student_id = document.querySelector('.content').dataset.id
	lesson_ids = new Map()
	token = document.getElementsByName('csrfmiddlewaretoken')[0].value
	for (lesson of lessons) {
		lesson_ids.set(lesson.value, lesson.checked)
	}
	lesson_ids = JSON.stringify(Object.fromEntries(lesson_ids))
	data = JSON.stringify({"data": JSON.stringify(lesson_ids)})
	response = await fetch('http://127.0.0.1:8000/' + student_id + '/save',{
		method: "POST",
		headers: {
      		"Content-Type": "application/json",
      		'X-CSRFToken': token
    	},
    	body: data
	})
	location.reload()
}

const show_payment_form = async (event) => {
	content = document.querySelector('.content')
	if (!!content) {
		student_id = document.querySelector('.content').dataset.id
	} else {
		student_id = this.event.target.dataset.id
	}
	// student_id = document.querySelector('.content').dataset.id
	token = document.getElementsByName('csrfmiddlewaretoken')[0].value
	response = await fetch('http://127.0.0.1:8000/' + student_id + '/payment_form');
	response.text().then((data) => {
		el = document.createElement('div')
		popup = el
		el.innerHTML = data
		document.body.appendChild(el)	
	})
}

const show_lesson_form = async (event) => {
	content = document.querySelector('.content')
	if (!!content) {
		student_id = document.querySelector('.content').dataset.id
	} else {
		student_id = this.event.target.dataset.id
	}
	// student_id = document.querySelector('.content').dataset.id
	token = document.getElementsByName('csrfmiddlewaretoken')[0].value
	response = await fetch('http://127.0.0.1:8000/' + student_id + '/lesson_form');
	response.text().then((data) => {
		el = document.createElement('div')
		popup = el
		el.innerHTML = data
		document.body.appendChild(el)	
	})
}

const close_form = () => {
	popup.remove()
}