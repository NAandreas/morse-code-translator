from flask import current_app, session, render_template
from . import main
from .forms import MorseForm, TextForm
from ..morse import to_morse, from_morse


@main.route('/', methods=['GET', 'POST'])
def index():
    """Default application route."""
    morse_form = MorseForm(prefix='morse_')
    text_form = TextForm(prefix='text_')

    morse = session.get('last_morse', None)
    if morse_form.submit.data and morse_form.validate_on_submit():
        current_app.logger.debug('Translating to morse code...')
        morse = to_morse(morse_form.text.data)
        session['last_morse'] = morse

    text = session.get('last_text', None)
    if text_form.submit.data and text_form.validate_on_submit():
        current_app.logger.debug('Translating from morse code...')
        text = from_morse(text_form.morse.data)
        session['last_text'] = text

    return render_template('index.html', morse_form=morse_form, morse=morse,
                                         text_form=text_form, text=text)
