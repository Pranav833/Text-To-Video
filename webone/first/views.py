from django.shortcuts import render
from django.http import HttpResponse
import time

from .forms import TextInputForm, PDFUploadForm
from .main import create_summary, generate_subtitles, generate_video, extract_text_from_pdf
from django.core.files.storage import default_storage
import os

def index(request):
    return HttpResponse("Hello, world!")


def get_input(request):
    if request.method == 'POST':
        text_form = TextInputForm(request.POST)
        pdf_form = PDFUploadForm(request.POST, request.FILES)

        if text_form.is_valid():
            text = text_form.cleaned_data["text"]
        elif pdf_form.is_valid():
            pdf_file = request.FILES['pdf_file']
            pdf_file_path = default_storage.save(f"pdf_files/{pdf_file.name}",pdf_file)
            print("saved")
            text = extract_text_from_pdf(pdf_file_path)
        else:
            return HttpResponse("Invalid Form Data")
        

        # print(text)

        words, summary = create_summary(text)
        # subtitles = generate_subtitles(summary)
        print([words,summary])

        for i,sentence in enumerate(summary):
            print(i,"--",sentence)

        print("\n\nextracted words")
        for i,word in enumerate(words):
            print(i,"--",word)

        final_clip = generate_video(words,summary)
        video_file_path = "videos/generated_video.mp4"
        video_file_full_path = os.path.join(default_storage.location, video_file_path)
        final_clip.write_videofile(video_file_full_path, codec="libx264", audio_codec="aac", fps=24)

        time.sleep(120)
    
    text_form = TextInputForm()
    pdf_form = PDFUploadForm()
    return render(request, 'inputpage.html', {'text_form': text_form, 'pdf_form': pdf_form})