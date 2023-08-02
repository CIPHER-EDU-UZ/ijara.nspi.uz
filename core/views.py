from django.shortcuts import render
from .models import Room, Student

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def student_list(request, room_id):
    room = Room.objects.get(pk=room_id)
    students = Student.objects.filter(room=room)
    occupied_seats = students.count()
    room.occupied_seats = occupied_seats
    room.save()
    return render(request, 'student_list.html', {'room': room, 'students': students})
