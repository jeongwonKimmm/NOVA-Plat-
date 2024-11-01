from django import forms
from .models import Department


# 학과 폼
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department  
        fields = ["name", "memo"]
        
    # 학과 검증
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("학과명을 입력해주세요.")
        if len(name) < 2 or len(name) > 20:
            raise forms.ValidationError("학과명은 2글자 이상, 20글자 이하로 입력해주세요.")
        return name
        
    # 메모 검증
    def clean_memo(self):
        memo = self.cleaned_data.get("memo")
        if len(memo) > 200:
            raise forms.ValidationError("메모는 200글자 이하로 입력해주세요.")
        return memo
        