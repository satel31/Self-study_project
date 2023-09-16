from django.db import models

from apps.user.models import User

NULLABLE = {'blank': True, 'null': True}


class Section(models.Model):
    section_name = models.CharField(max_length=235, verbose_name='Section name')
    preview = models.ImageField(upload_to='sections/', verbose_name='Sections preview', **NULLABLE)
    description = models.TextField(verbose_name='Section description', **NULLABLE)

    def __str__(self):
        return f'{self.section_name}'

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class Material(models.Model):
    material_name = models.CharField(max_length=235, verbose_name='Material name')
    description = models.TextField(verbose_name='Material description', **NULLABLE)
    preview = models.ImageField(upload_to='materials/', verbose_name='Material preview', **NULLABLE)
    text = models.TextField(verbose_name='Material text')
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, verbose_name='Section', **NULLABLE,
                                related_name='material')

    def __str__(self):
        return f'{self.material_name}'

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materials'


class Test(models.Model):
    test_name = models.CharField(max_length=255, verbose_name='Test name')
    description = models.TextField(verbose_name='Test description')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Material of the test', **NULLABLE,
                                 related_name='tests')

    def __str__(self):
        return f'{self.test_name}'

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Test', related_name='questions')
    text = models.CharField(max_length=500, verbose_name='Text of the question')

    def __str__(self):
        return f'Question of {self.test}'

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question', )
    text = models.CharField(max_length=500, verbose_name='Text of the answer')

    def __str__(self):
        return f'Answer of {self.question}'

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'


class UserAnswer(models.Model):
    answer = models.CharField(max_length=500, verbose_name='Text of the answer')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question',
                                 related_name='user_answers')
    is_passed = models.BooleanField(default=False, verbose_name='Is passed')

    def __str__(self):
        return f'{self.user} {self.question} {self.answer}'

    class Meta:
        verbose_name = 'user_answer'
        verbose_name_plural = 'user_answers'
