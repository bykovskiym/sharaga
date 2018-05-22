/**
 */
package lv.vogella.webpage.model.webpage;

import java.util.Calendar;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Article</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link lv.vogella.webpage.model.webpage.Article#getName <em>Name</em>}</li>
 *   <li>{@link lv.vogella.webpage.model.webpage.Article#getCreated <em>Created</em>}</li>
 * </ul>
 *
 * @see lv.vogella.webpage.model.webpage.WebpagePackage#getArticle()
 * @model
 * @generated
 */
public interface Article extends EObject {
	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Name</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see lv.vogella.webpage.model.webpage.WebpagePackage#getArticle_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link lv.vogella.webpage.model.webpage.Article#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Created</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Created</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Created</em>' attribute.
	 * @see #setCreated(Calendar)
	 * @see lv.vogella.webpage.model.webpage.WebpagePackage#getArticle_Created()
	 * @model dataType="lv.vogella.webpage.model.webpage.Calendar"
	 * @generated
	 */
	Calendar getCreated();

	/**
	 * Sets the value of the '{@link lv.vogella.webpage.model.webpage.Article#getCreated <em>Created</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Created</em>' attribute.
	 * @see #getCreated()
	 * @generated
	 */
	void setCreated(Calendar value);

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @model annotation="http://www.eclipse.org/emf/2002/GenModel body='if (eIsProxy()) return super.toString();\r\n\r\n        StringBuffer result = new StringBuffer(super.toString());\r\n        result.append(\" (name: \");\r\n        result.append(name);\r\n        result.append(\", created: \");\r\n        result.append(created);\r\n        result.append(\')\');\r\n        return result.toString();'"
	 * @generated
	 */
	String toString();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @model annotation="http://www.eclipse.org/emf/2002/GenModel body='return 42 + input;'"
	 * @generated
	 */
	int test(int input);

} // Article
