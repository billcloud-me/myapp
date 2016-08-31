package com.billcloud.web.hodor;

import static org.junit.Assert.*;

import org.junit.Test;

public class MyHodorTest {

	@Test
	public void testHodor() {
		MyHodor hodor = new MyHodor();
		String result = hodor.question();
		assertEquals("Hodor!", result);
	}

}
