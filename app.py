import os
import ktrain
from ktrain import text
from hlprs.func_cmp import __API_KEY as pkpk
from hlprs.func_cmp import Comparator
from flask import Flask, render_template, render_template_string, redirect, url_for, request
# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/compare')
def cmp_view():
    return render_template('compare.html')


@app.route('/sentiment')
def stmt_view():
    return render_template('sentiment.html')


@app.route('/comparation-result/<res_cmp>/<prox>')
def success(res_cmp, prox):
    #  return 'welcome %s' % name
    return render_template('compared.html', cmp_res=res_cmp, percent=prox)


@app.route('/comparated', methods=['POST', 'GET'])
def comparated():
    apikey = pkpk
    if request.method == 'POST':
        comparator1 = request.form['cmpr1']
        comparator2 = request.form['cmpr2']

        cmpr = Comparator()

        if request.form['cats'] == 'url_comp':
            result = cmpr.compare_urls(apikey, comparator1, comparator2)
        else:
            result = cmpr.compare_text(apikey, comparator1, comparator2)
        proxm = result.get_proximity()

        if proxm >= 1.0:
            status = 'EXACTLY THE SAME'
        elif proxm > 0.7:
            status = 'HIGH'
        elif proxm > .5:
            status = 'MEDIUM'
        elif proxm > 0:
            status = 'LOW'
        else:
            status = 'NOT THE SAME AT ALL'
        return redirect(url_for('success', res_cmp=status, prox=round(proxm*100, 2)))
    else:
        user = request.args.get('cmpr1')
        return redirect(url_for('success', res_cmp=user))


@app.route('/sentiment-result/<res_cmp>/<prox>')
def success_stmt(res_cmp, prox):
    #  return 'welcome %s' % name
    return render_template('sentimented.html', stmt_res=res_cmp, percent=prox)


@app.route('/sentimented', methods=['POST', 'GET'])
def sentimented():
    predictor = ktrain.load_predictor('sntmt_model')

    if request.method == 'POST':
        stmt_text = request.form['sntmt1']
        res_pred = predictor.predict(stmt_text)
        prob_pred = predictor.predict(stmt_text, return_proba=True)

        if res_pred == 0:
            status = 'Negative'
            proxm = prob_pred[0]
        else:
            status = status = 'Positive'
            proxm = prob_pred[1]
        return redirect(url_for('success_stmt', res_cmp=status, prox=round(proxm*100, 2)))
    else:
        user = request.args.get('sntmt1')
        return redirect(url_for('success_stmt', res_cmp=user))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error_404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return render_template('error_500.html'), 500


if __name__ == '__main__':
    app.run()
