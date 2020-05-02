using System;
using System.Configuration;
using System.Security.Cryptography;
using System.Text;

public class Program
{
	    public static string Decrypt(string cipherString, bool useHashing)
        {
            byte[] array = Convert.FromBase64String(cipherString);
            AppSettingsReader appSettingsReader = new AppSettingsReader();
            string s = "_5TL#+GWWFv6pfT3!GXw7D86pkRRTv+$$tk^cL5hdU%";
            byte[] key;
            if (useHashing)
            {
                MD5CryptoServiceProvider md5CryptoServiceProvider = new MD5CryptoServiceProvider();
                key = md5CryptoServiceProvider.ComputeHash(Encoding.UTF8.GetBytes(s));
                md5CryptoServiceProvider.Clear();
            }
            else
            {
                key = Encoding.UTF8.GetBytes(s);
            }
            TripleDESCryptoServiceProvider tripleDESCryptoServiceProvider = new TripleDESCryptoServiceProvider();
            tripleDESCryptoServiceProvider.Key = key;
            tripleDESCryptoServiceProvider.Mode = CipherMode.ECB;
            tripleDESCryptoServiceProvider.Padding = PaddingMode.PKCS7;
            ICryptoTransform cryptoTransform = tripleDESCryptoServiceProvider.CreateDecryptor();
            byte[] bytes = cryptoTransform.TransformFinalBlock(array, 0, array.Length);
            tripleDESCryptoServiceProvider.Clear();
            return Encoding.UTF8.GetString(bytes);
        }
	
	
	public static void Main()
	{
		Console.WriteLine( Decrypt("oQ5iORgUrswNRsJKH9VaCw==", true) );
	}
}
