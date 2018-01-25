package DSA;

import com.sun.org.apache.xerces.internal.impl.dv.util.HexBin;

import java.security.*;
import java.security.interfaces.DSAPrivateKey;
import java.security.interfaces.DSAPublicKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;

public class Dsa {
    public static String src = "hello berber" ;
    public static void main(String[] args) {
            jdkDSA();
    }
    public static void jdkDSA(){
        try{
            // 初始化：
            KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DSA") ;
            keyPairGenerator.initialize(512);
            KeyPair keyPair = keyPairGenerator.generateKeyPair();

            DSAPublicKey dsaPublicKey = (DSAPublicKey)keyPair.getPublic() ;
            DSAPrivateKey dsaPrivateKey = (DSAPrivateKey)keyPair.getPrivate() ;
            // 签名：
            PKCS8EncodedKeySpec pkcs8EncodedKeySpec = new PKCS8EncodedKeySpec(dsaPrivateKey.getEncoded());
            KeyFactory keyFactory = KeyFactory.getInstance("DSA");
            PrivateKey privateKey = keyFactory.generatePrivate(pkcs8EncodedKeySpec);
            Signature signature = Signature.getInstance("SHA1withDSA");
            signature.initSign(privateKey);
            signature.update(src.getBytes());
            byte arr[] = signature.sign() ;
            System.out.println("jdk dsa sign:"+ HexBin.encode(arr));
            // 验证签名
            X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(dsaPublicKey.getEncoded()) ;
            keyFactory = KeyFactory.getInstance("DSA");
            PublicKey publicKey = keyFactory.generatePublic(x509EncodedKeySpec) ;
            signature = Signature.getInstance("SHA1withDSA");
            signature.initVerify(publicKey);
            signature.update(src.getBytes());
            boolean bool = signature.verify(arr) ;
            System.out.println("jdk dsa verify:"+bool);
        }catch (Exception e){

        }
    }
}
