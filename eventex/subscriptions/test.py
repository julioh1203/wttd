from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')


    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """HTML must contain input tags """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_has_form(self):
        """HTML must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribeSuccessPost(TestCase):
    def setUp(self):
        data = {'name':'Julio', 'cpf': '12345678901',
                'email': 'monitoramento@octaltecnologia.com.br', 'phone': '15-3524-3944'}
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(self.response.status_code, 302)

    def test_send_subscribe_email(self):
        self.assertEqual(len(mail.outbox), 1)

    def test_subscribe_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(email.subject, expect)

    def test_subscribe_email_from(self):
        email = mail.outbox[0]
        expect = 'monitoramento@octaltecnologia.com.br'

        self.assertEqual(email.from_email, expect)

    def test_subscribe_email_to(self):
        email = mail.outbox[0]
        expect = ['monitoramento@octaltecnologia.com.br', 'contato@eventex.com.br']

        self.assertEqual(email.to, expect)

    def test_subscribe_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Julio', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('monitoramento@octaltecnologia.com.br', email.body)
        self.assertIn('15-3524-3944', email.body)


class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """The template should be subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_form(self):
        """The page must include the form in the context"""
        form = self.response.context['form']

        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        """The form should contain errors"""
        form = self.response.context['form']

        self.assertTrue(form.errors)

class SubscribeSuccessfulMessage(TestCase):
    def test_message(self):
        data = {'name':'Julio', 'cpf': '12345678901',
                'email': 'monitoramento@octaltecnologia.com.br', 'phone': '15-3524-3944'}
        response = self.client.post('/inscricao/', data, follow=True)

        self.assertContains(response, 'Inscrição realizada com sucesso!')




