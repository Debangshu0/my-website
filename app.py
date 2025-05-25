from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import os
import math as Amitisgay
app = Flask(__name__)
app.secret_key = 'you_are_gay'
@app.route('/list-files')
def list_files():
    files = os.listdir('templates')
    return "<br>".join(files)
def cofactor(matrix):
    n = matrix.shape[0]
    cofactors = np.zeros_like(matrix, dtype=float)
    
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    
    return cofactors

@app.route('/', methods=['GET', 'POST'])
def home():
    # result = None
    # if request.method == 'POST':
    #     try:
    #         num1 = float(request.form['num1'])
    #         num2 = float(request.form['num2'])
    #         operation = request.form['operation']

    #         if operation == 'add':
    #             result = num1 + num2
    #         elif operation == 'multiply':
    #             result = num1 * num2
    #         else:
    #             result = "Invalid Operation"

    #         # Redirect to result page with the result as a query parameter
    #         return redirect(url_for('result', result=result))

    #     except ValueError:
    #         result = "Invalid input"

    #  return render_template('dynamic.html', result=result)
    data=[]
    order=""
    total_items=[]
    b=5
    matrixoutput=None
    matrix0=[]
    a=None
    operation=None
    finaloutput=[]
    listkicker=None
    zkicker=None
    development=0
    invalider=None
    session['order']=session.get('order',order)
    session['total_items']=session.get('total_items',total_items)
    session['b']=session.get('b',0)
    if request.method == 'POST':
      if 'order' in request.form:
        order = request.form['order']
        session['total_items']=[]
        session['a']=a=int((order.partition("X"))[0])#row
        session['b']=b=int((order.partition("X"))[2])#column
        for i in range(a*b):total_items.append(i+1)
        session['total_items']=total_items
        session['order']=order

        #data storage
        for i in range((a*b)+1):
          data.append(request.form.get(f"item_{i}"))
      else:
        order = session.get('order', '')
        total_items = session.get('total_items', [])
        a = session.get('a', 0)
        b = session.get('b', 0)
        for i in range((a * b)+1):
          data.append(request.form.get(f"item_{i}"))
      data.pop(0)
      try:
        if data[2]==None:raise TypeError("None list")
        data = [int(i) for i in data]
      except ValueError:
        data="Invalid input"
      except TypeError:
        pass      
      rows_list = []
      appender = []

      for i in data:
        appender.append(i)
        if len(appender) == b:
            rows_list.append(appender)
            appender = []

    # Now convert once to a numpy array with float dtype
      matrix0 = np.array(rows_list, dtype=float)
      operation=request.form.get('operation')
      if operation=="Trans":
        matrixoutput=matrix0.T
      elif operation=="Inv":
        if a!=b:
          matrixoutput="INVALID"
        elif np.linalg.det(matrix0)==0:
          matrixoutput="INVALID"
        else:
          matrixoutput=np.round(np.linalg.inv(matrix0), 2)
      elif operation=="Det":
        matrixoutput=round(np.linalg.det(matrix0), 2)
      elif operation=="Cof":
        if a!=b:
          matrixoutput="INVALID"
        else:
          matrixoutput=cofactor(matrix0)
      elif operation=="Adj":
        if a!=b:
          matrixoutput="INVALID"
        else:
          matrixoutput=(cofactor(matrix0)).T
      elif (operation=="Scal") or (operation=="Add") or (operation=="Subtract") or (operation=="Multi") or (operation=="Some"):
        matrixoutput="UNDER DEVELOPMENT !!"
      else:matrixoutput="Oops! Something went wrong"
      # return redirect(url_for('result', matrixoutput=matrixoutput))
      if type(matrixoutput)==np.ndarray:
        for i in matrixoutput:
          for j in i:
           if float(j)==int(j):
             finaloutput.append(int(j))
           else:
             finaloutput.append(round(float(j),1))
          listkicker=1
      elif type(matrixoutput)==np.float64:
        if matrixoutput-(int(matrixoutput)):finaloutput=matrixoutput
        else:finaloutput=round(matrixoutput,2)
        zkicker=1
      if type(matrixoutput)==str:
        if matrixoutput=="INVALID":
          invalider=1
          listkicker=1
      #for now temporarily using this
      if (operation=="Scal") or (operation=="Add") or (operation=="Subtract") or (operation=="Multi"):
        development=1
      elif (operation=="Some"):
        development=2
    return render_template('dynamic.html',order=order,total_items=total_items,a=a,b=b,matrixoutput=matrixoutput,matrix0=matrix0,operation=operation,finaloutput=finaloutput,listkicker=listkicker,zkicker=zkicker,development=development, invalider=invalider, data=data, session=session)

@app.route('/surprise')
def surprise():
    return render_template('surprise.html')
    


        

# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     matrixoutput = request.args.get('matrixoutput', '')
#     return render_template('result.html', matrixoutput=matrixoutput)

if __name__ == '__main__':
    app.run(debug=True)
















