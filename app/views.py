from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Question, Answer
from .forms import UserRegisterForm, QuestionForm, AnswerForm

# Create your views here.
def home(request):
    return render (request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'app/templates/register.html', {'form': form})


class QuestionListView(ListView):
    model = Question
    template_name = 'app/templates/home.html'
    context_object_name = 'questions'
    paginate_by = 10

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'app/templates/question_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_form'] = AnswerForm()
        return context
    

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'app/templates/ask_question.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

@login_required
def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            messages.success(request, 'Your answer has been posted!')
            return redirect('question-detail', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'app/templates/question_detail.html', {'question': question, 'form': form})


@login_required
def like_toggle(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        answer_id = request.POST.get('id')
        answer = get_object_or_404(Answer, id=answer_id)
        
        if request.user in answer.likes.all():
            answer.likes.remove(request.user)
            liked = False
        else:
            answer.likes.add(request.user)
            liked = True
            
        context = {
            'answer': answer,
            'liked': liked,
            'total_likes': answer.total_likes(),
        }
        
        data = {
            'liked': liked,
            'total_likes': answer.total_likes(),
        }
        
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)