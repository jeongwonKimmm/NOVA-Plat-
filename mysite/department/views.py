from django.http import HttpResponse
from django.shortcuts import render

# 학과 목록
def department_list(request):
    return HttpResponse("학과 목록")

# 학과 등록
def department_create(request):
    return HttpResponse("학과 등록")

# 학과 상세보기
def department_read(request):
    return HttpResponse("학과 상세보기")

# 학과 수정
def department_update(request):
    return HttpResponse("학과 수정")

# 학과 삭제
def department_delete(request):
    return HttpResponse("학과 삭제")
