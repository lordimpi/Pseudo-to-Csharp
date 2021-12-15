Using System;

	class program
	{
			int suma  (entero  _operando1, int _operando2){
			return _operando1 + _operando2;
			}
			 
			int resta  (entero  _operando1, int _operando2){
			return _operando1 - _operando2;
			}
		void Main(string[] args)
		{
			int _opcion=1;
			int _operando1=5;
			int _operando2=4;
			switch (_opcion){
			case 1:
			 _response = suma  (_operando1,_operando2);
			Console.WriteLine ("el  resultado  de  la  suma  es:  ",  _response);
			break;
			case 2:
			 _response = resta  (_operando1,_operando2);
			Console.WriteLine ("el  resultado  de  la  resta  es:  ",  _response);
			break;
			default:
			Console.WriteLine ("Opción  no  válida");
			}
		}
	}
