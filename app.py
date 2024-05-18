from flask import Flask, render_template, request
from news_fetcher.facade.google_news_facade import get_news

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        search_in = request.form.get('search_in')
        sources = request.form.get('sources')
        domains = request.form.get('domains')
        exclude_domains = request.form.get('exclude_domains')
        from_date = request.form.get('from_date')
        to_date = request.form.get('to_date')
        language = request.form.get('language')
        sort_by = request.form.get('sort_by')
        page_size = int(request.form.get('page_size'))
        
        # Fetch news based on form inputs
        news_data = get_news(
            keywords=keywords,
            search_in=search_in,
            sources=sources,
            domains=domains,
            exclude_domains=exclude_domains,
            from_date=from_date,
            to_date=to_date,
            language=language,
            sort_by=sort_by,
            page_size=page_size
        )
        
        return render_template('index.html', news_data=news_data, keywords=keywords, search_in=search_in, sources=sources, domains=domains, exclude_domains=exclude_domains, from_date=from_date, to_date=to_date, language=language, sort_by=sort_by, page_size=page_size)
    else:
        # Default news
        news_data = get_news()
        return render_template('index.html', news_data=news_data)

if __name__ == '__main__':
    app.run(debug=True)
